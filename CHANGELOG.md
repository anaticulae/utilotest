# Changelog

Every noteable change is logged here.

## v0.24.1 (2022-10-28)

### Fix

* ensure to setup API as str (0dc3a33bebc3)

### Chore

* upgrade environment (e75b34bbaf11)
* upgrade requirements.txt (f830a4910db8)

## v0.24.0 (2022-10-15)

### Feature

* enable more than one expected bin (4bbb68c9ab1c)

### Chore

* upgrade baw (4399fe7a46ab)

## v0.23.0 (2022-10-09)

### Feature

* add separate marker selector (277f11e3af0d)

### Chore

* publish test report (99f5f1ef349e)
* convert longrun to all (460014c27c8f)
* upgrade requirements.txt (9dad0ffae883)

## v0.22.0 (2022-10-05)

### Feature

* use marker to select unit tests (0aed2f85fdfa)

### Chore

* upgrade baw (fbcdd01e42e6)
* root user is not required (4b62ec495f3e)
* upgrade requirements.txt (134ccb372809)

## v0.21.0 (2022-10-03)

### Feature

* add monday selector to run very very large tests (f588365a8b1a)

## v0.20.1 (2022-09-28)

### Feature

* add worker max count to limit CI worker (d6ea48b9987e)

## v0.20.0 (2022-09-28)

### Feature

* add method to verify that test is running on CI (5cdd399f73a1)

### Fix

* detect CI on jenkins (f100cf4aadf0)

## v0.19.0 (2022-09-28)

### Feature

* add method to determine worker count depending on platform (360ecc52520d)

### Chore

* upgrade requirements.txt (e689d490826f)

## 0.18.0 auto generated release

### Feature

* ensure that geckodriver is in path (cfa4b2ef010a)
* add selector to select different platforms (f314fa24c05c)

## v0.17.0

### Fix

* skip view test on linux (14b3bd1971c1)

## v0.16.0

### Feature

* add marker to skip test if baw is not installed (ea6fe0e42040)
* add selector to skip tests if git is not installed (9953f708390a)

## v0.15.4

## v0.15.3

### Feature

* add None option to skip check (b06fa1842980)

## v0.15.2

## v0.15.1

## v0.15.0

### Feature

* add monkeypatch and testdir shortcuts (b8ad37a3ef78)

## v0.14.0

### Feature

* skip resource if not generated (39bd01ce7f63)
* add method to select test resources (ce86e76df165)
* detect invalid cli invocation (1a88f6276309)

## v0.13.0

### Feature

* add method to determine current test id (778584c285db)

## v0.12.4

### Feature

* add callable to run on failure (ef34f4ad2396)
* store source for later processing (c38a7840f60c)

## v0.12.3

### Feature

* add template to create basic test runner (6c3e4bb85a84)

## v0.12.2

### Feature

* improve decorator naming (a10c7a69f4e6)

## v0.12.1

### Fix

* rstrip to support spaces at start of expected document (27acc8ba1013)
* fix state converter (02019db06338)

## v0.12.0

### Feature

* add option to overwrite source to ease debugging (26b3442dbc5b)
* verify that power is installed (795e4f3c9d80)
* add selenium driver shortcut (c0654b7f8be6)

### Documentation

* Happy New Year! (d888cc76974f)
* fix modules path (6d9cd1df1329)

## v0.11.0

### Feature

* add parameter to compress lines of code (ab213a773192)
* check resource existence (4e1889ea72e3)
* add print_return decorator to print result (c53c0cefbff4)

## v0.10.1

### Feature

* add option to use pdf path as source (127e642b749a)

## v0.10.0

### Feature

* add baseline runner to ease verification step (a2043ce08eb8)

### Fix

* ensure that extension use correctly (62e7293af94e)

## v0.9.0

### Feature

* move tracer from train project (9344fc095a1c)

## v0.8.4

### Fix

* increase ast depth to use in more inherited environments (60f19e3bbf75)
* improve developer feedback (0da7d6d2641e)

## v0.8.3

### Feature

* add method to verify binary data (72cb9c2bbdd6)

## v0.8.2

### Fix

* enable recursive mode (dca30f899696)

## v0.8.1

### Fix

* support testdir.tmpath as input (04d2bf8b7297)

## v0.8.0

### Feature

* support multiple resources (6baebe7b42c8)

### Fix

* make filecount cwd independent (0322b57e5ac7)

## v0.7.1

### Feature

* add method to skip not as a decorator (fd5d11271462)

## v0.7.0

### Feature

* add option to verify non power-generated path (777ac70da499)
* add method to skip test if resource does not exists (96390e939f72)
* support CompletedProcess to stdout/stderr (295eb2b6b0d2)

## v0.6.0

### Feature

* add delete method (8916f2d85182)

## v0.5.3

## v0.5.2

## v0.5.1

### Fix

* add missing data delivery flag (5d68cf50a430)

## v0.5.0

### Feature

* add decorator to mark selenium tests (ce93a09d0c4c)
* add driver to fixture to run selenium (e36ee84513b0)
* add firefox driver (07e01820d747)

## v0.4.1

### Fix

* improve call assertion (84744d389905)

## v0.4.0

### Feature

* use parameter to shrink simplified name (a22c9835f179)
* add method to ease and secure generated test names (8b48e3a8d085)

## v0.3.2

### Fix

* return correct registered marker (d087a43442f5)

## v0.3.1

### Feature

* add method to register marker (edcae5f5a496)

### Documentation

* Happy New Year! (48de95e15ba4)

## v0.3.0

### Fix

* bypass marker check of new pytest version (cc7ced949ee4)

## v0.2.2

## v0.2.1

### Feature

* add method to setup prefix (1c1c708400e3)

## v0.2.0

### Feature

* add calls to test CRUD APIs (8299dd52ad08)
* add methods to analyze pytest stdout/stderr (76f72b2547cf)
* add holyvalue test selector (26a6b471caff)

## v0.1.6

### Feature

* introduce more intuitive selection decorator (490d4e732a44)

## v0.1.5

## v0.1.4

### Fix

* clarify error message (81de8fdaa795)

## v0.1.3

## v0.1.2

## v0.1.1

## v0.1.0

### Feature

* move test features from utila package (f94c51defd72)

## v0.0.0 Initial release

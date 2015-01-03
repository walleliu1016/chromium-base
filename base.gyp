{
  'targets': [
    {
      'target_name': 'base',
      'includes': [
        # Rules for excluding e.g. foo_win.cc from the build on non-Windows.
        'filename_rules.gypi',
      ],
      'type': 'static_library',
      'direct_dependent_settings': {
        'include_dirs': [
          'src',
        ],
        'xcode_settings': {
          'CLANG_CXX_LANGUAGE_STANDARD': 'gnu++11',
          'CLANG_CXX_LIBRARY': 'libstdc++',
        },
        'cflags_cc': [
          '-std=c++0x',
        ],
        'conditions': [
          ['OS=="linux"', {
            'ldflags': [
              '-pthread',
            ],
          }],
        ],
      },
      'include_dirs': [
        'src',
      ],
      'xcode_settings': {
        'CLANG_CXX_LANGUAGE_STANDARD': 'gnu++11',
        'CLANG_CXX_LIBRARY': 'libstdc++',
      },
      'cflags_cc': [
        '-std=c++0x',
      ],
      'dependencies': [
        'src/third_party/libevent/libevent.gyp:libevent'
      ],
      # In Chromium code, we define __STDC_foo_MACROS in order to get the
      # C99 macros on Mac and Linux.
      'defines': [
        '__STDC_CONSTANT_MACROS',
        '__STDC_FORMAT_MACROS',
      ],
      'sources': [
        'src/base/at_exit.cc',
        'src/base/at_exit.h',
        'src/base/atomic_ref_count.h',
        'src/base/atomicops.h',
        'src/base/atomicops_internals_arm_gcc.h',
        'src/base/atomicops_internals_atomicword_compat.h',
        'src/base/atomicops_internals_gcc.h',
        'src/base/atomicops_internals_mac.h',
        'src/base/atomicops_internals_mips_gcc.h',
        'src/base/atomicops_internals_tsan.h',
        'src/base/atomicops_internals_x86_gcc.cc',
        'src/base/atomicops_internals_x86_gcc.h',
        'src/base/atomicops_internals_x86_msvc.h',
        'src/base/base_export.h',
        'src/base/base_switches.cc',
        'src/base/base_switches.h',
        'src/base/basictypes.h',
        'src/base/bind.h',
        'src/base/bind_helpers.cc',
        'src/base/bind_helpers.h',
        'src/base/bind_internal.h',
        'src/base/bind_internal_win.h',
        'src/base/callback.h',
        'src/base/callback_forward.h',
        'src/base/callback_helpers.cc',
        'src/base/callback_helpers.h',
        'src/base/callback_internal.cc',
        'src/base/callback_internal.h',
        'src/base/callback_registry.h',
        'src/base/cancelable_callback.h',
        'src/base/command_line.cc',
        'src/base/command_line.h',
        'src/base/compiler_specific.h',
        'src/base/containers/hash_tables.h',
        'src/base/containers/linked_list.h',
        'src/base/containers/mru_cache.h',
        'src/base/containers/scoped_ptr_hash_map.h',
        'src/base/containers/small_map.h',
        'src/base/containers/stack_container.h',
        'src/base/debug/alias.cc',
        'src/base/debug/alias.h',
        'src/base/debug/asan_invalid_access.cc',
        'src/base/debug/asan_invalid_access.h',
        'src/base/debug/crash_logging.cc',
        'src/base/debug/crash_logging.h',
        'src/base/debug/debugger.cc',
        'src/base/debug/debugger.h',
        'src/base/debug/debugger_posix.cc',
        'src/base/debug/dump_without_crashing.cc',
        'src/base/debug/dump_without_crashing.h',
        'src/base/debug/leak_annotations.h',
        'src/base/debug/leak_tracker.h',
        'src/base/debug/proc_maps_linux.cc',
        'src/base/debug/proc_maps_linux.h',
        'src/base/debug/profiler.cc',
        'src/base/debug/profiler.h',
        'src/base/debug/stack_trace.cc',
        'src/base/debug/stack_trace.h',
        'src/base/debug/stack_trace_posix.cc',
        'src/base/debug/task_annotator.cc',
        'src/base/debug/task_annotator.h',
        'src/base/debug/trace_event.h',
        'src/base/debug/trace_event_argument.cc',
        'src/base/debug/trace_event_argument.h',
        'src/base/debug/trace_event_impl.cc',
        'src/base/debug/trace_event_impl.h',
        'src/base/debug/trace_event_impl_constants.cc',
        'src/base/debug/trace_event_memory.cc',
        'src/base/debug/trace_event_memory.h',
        'src/base/debug/trace_event_synthetic_delay.cc',
        'src/base/debug/trace_event_synthetic_delay.h',
        'src/base/debug/trace_event_system_stats_monitor.cc',
        'src/base/debug/trace_event_system_stats_monitor.h',
        'src/base/files/file_path.cc',
        'src/base/files/file_path.h',
        'src/base/files/file_path_constants.cc',
        'src/base/json/json_file_value_serializer.cc',
        'src/base/json/json_file_value_serializer.h',
        'src/base/json/json_parser.cc',
        'src/base/json/json_parser.h',
        'src/base/json/json_reader.cc',
        'src/base/json/json_reader.h',
        'src/base/json/json_string_value_serializer.cc',
        'src/base/json/json_string_value_serializer.h',
        'src/base/json/json_value_converter.cc',
        'src/base/json/json_value_converter.h',
        'src/base/json/json_writer.cc',
        'src/base/json/json_writer.h',
        'src/base/json/string_escape.cc',
        'src/base/json/string_escape.h',
        'src/base/lazy_instance.cc',
        'src/base/lazy_instance.h',
        'src/base/location.cc',
        'src/base/location.h',
        'src/base/logging.cc',
        'src/base/logging.h',
        'src/base/memory/raw_scoped_refptr_mismatch_checker.h',
        'src/base/memory/ref_counted.cc',
        'src/base/memory/ref_counted.h',
        'src/base/memory/ref_counted_memory.cc',
        'src/base/memory/ref_counted_memory.h',
        'src/base/memory/scoped_handle.h',
        'src/base/memory/scoped_policy.h',
        'src/base/memory/scoped_ptr.h',
        'src/base/memory/scoped_vector.h',
        'src/base/memory/singleton.cc',
        'src/base/memory/singleton.h',
        'src/base/memory/weak_ptr.cc',
        'src/base/memory/weak_ptr.h',
        'src/base/message_loop/incoming_task_queue.cc',
        'src/base/message_loop/incoming_task_queue.h',
        'src/base/message_loop/message_loop.cc',
        'src/base/message_loop/message_loop.h',
        'src/base/message_loop/message_loop_proxy.cc',
        'src/base/message_loop/message_loop_proxy.h',
        'src/base/message_loop/message_loop_proxy_impl.cc',
        'src/base/message_loop/message_loop_proxy_impl.h',
        'src/base/message_loop/message_pump.cc',
        'src/base/message_loop/message_pump.h',
        'src/base/message_loop/message_pump_default.cc',
        'src/base/message_loop/message_pump_default.h',
        'src/base/message_loop/message_pump_libevent.cc',
        'src/base/message_loop/message_pump_libevent.h',
        'src/base/message_loop/timer_slack.h',
        'src/base/move.h',
        'src/base/pending_task.cc',
        'src/base/pending_task.h',
        'src/base/pickle.cc',
        'src/base/pickle.h',
        'src/base/port.h',
        'src/base/process/process_handle.h',
        'src/base/process/process_handle_linux.cc',
        'src/base/process/process_handle_posix.cc',
        'src/base/profiler/alternate_timer.cc',
        'src/base/profiler/alternate_timer.h',
        'src/base/profiler/tracked_time.cc',
        'src/base/profiler/tracked_time.h',
        'src/base/run_loop.cc',
        'src/base/run_loop.h',
        'src/base/safe_strerror_posix.cc',
        'src/base/safe_strerror_posix.h',
        'src/base/scoped_clear_errno.h',
        'src/base/sequence_checker.h',
        'src/base/sequence_checker_impl.cc',
        'src/base/sequence_checker_impl.h',
        'src/base/sequenced_task_runner.cc',
        'src/base/sequenced_task_runner.h',
        'src/base/stl_util.h',
        'src/base/strings/string16.cc',
        'src/base/strings/string16.h',
        'src/base/strings/string_number_conversions.cc',
        'src/base/strings/string_number_conversions.h',
        'src/base/strings/string_piece.cc',
        'src/base/strings/string_piece.h',
        'src/base/strings/string_split.cc',
        'src/base/strings/string_split.h',
        'src/base/strings/string_tokenizer.h',
        'src/base/strings/string_util.cc',
        'src/base/strings/string_util.h',
        'src/base/strings/string_util_constants.cc',
        'src/base/strings/string_util_posix.h',
        'src/base/strings/string_util_win.h',
        'src/base/strings/stringize_macros.h',
        'src/base/strings/stringprintf.cc',
        'src/base/strings/stringprintf.h',
        'src/base/strings/sys_string_conversions.h',
        'src/base/strings/sys_string_conversions_posix.cc',
        'src/base/strings/utf_string_conversion_utils.cc',
        'src/base/strings/utf_string_conversion_utils.h',
        'src/base/strings/utf_string_conversions.cc',
        'src/base/strings/utf_string_conversions.h',
        'src/base/synchronization/cancellation_flag.cc',
        'src/base/synchronization/cancellation_flag.h',
        'src/base/synchronization/condition_variable.h',
        'src/base/synchronization/condition_variable_posix.cc',
        'src/base/synchronization/lock.cc',
        'src/base/synchronization/lock.h',
        'src/base/synchronization/lock_impl.h',
        'src/base/synchronization/lock_impl_posix.cc',
        'src/base/synchronization/waitable_event.h',
        'src/base/synchronization/waitable_event_posix.cc',
        'src/base/sys_info.cc',
        'src/base/sys_info.h',
        'src/base/sys_info_linux.cc',
        'src/base/sys_info_posix.cc',
        'src/base/task_runner.cc',
        'src/base/task_runner.h',
        'src/base/template_util.h',
        'src/base/third_party/dmg_fp/dmg_fp.h',
        'src/base/third_party/dmg_fp/dtoa_wrapper.cc',
        'src/base/third_party/dmg_fp/g_fmt.cc',
        'src/base/third_party/dynamic_annotations/LICENSE',
        'src/base/third_party/dynamic_annotations/README.chromium',
        'src/base/third_party/dynamic_annotations/dynamic_annotations.c',
        'src/base/third_party/dynamic_annotations/dynamic_annotations.gyp',
        'src/base/third_party/dynamic_annotations/dynamic_annotations.h',
        'src/base/third_party/icu/icu_utf.cc',
        'src/base/third_party/icu/icu_utf.h',
        'src/base/third_party/nspr/prtime.cc',
        'src/base/third_party/nspr/prtime.h',
        'src/base/third_party/valgrind/memcheck.h',
        'src/base/third_party/valgrind/valgrind.h',
        'src/base/thread_task_runner_handle.cc',
        'src/base/thread_task_runner_handle.h',
        'src/base/threading/non_thread_safe.h',
        'src/base/threading/non_thread_safe_impl.cc',
        'src/base/threading/non_thread_safe_impl.h',
        'src/base/threading/platform_thread.h',
        'src/base/threading/platform_thread_linux.cc',
        'src/base/threading/platform_thread_posix.cc',
        'src/base/threading/platform_thread_win.cc',
        'src/base/threading/post_task_and_reply_impl.cc',
        'src/base/threading/post_task_and_reply_impl.h',
        'src/base/threading/sequenced_worker_pool.cc',
        'src/base/threading/sequenced_worker_pool.h',
        'src/base/threading/simple_thread.cc',
        'src/base/threading/simple_thread.h',
        'src/base/threading/thread.cc',
        'src/base/threading/thread.h',
        'src/base/threading/thread_checker.h',
        'src/base/threading/thread_checker_impl.cc',
        'src/base/threading/thread_checker_impl.h',
        'src/base/threading/thread_collision_warner.cc',
        'src/base/threading/thread_collision_warner.h',
        'src/base/threading/thread_id_name_manager.cc',
        'src/base/threading/thread_id_name_manager.h',
        'src/base/threading/thread_local.h',
        'src/base/threading/thread_local_posix.cc',
        'src/base/threading/thread_local_storage.cc',
        'src/base/threading/thread_local_storage.h',
        'src/base/threading/thread_local_storage_posix.cc',
        'src/base/threading/thread_restrictions.cc',
        'src/base/threading/thread_restrictions.h',
        'src/base/time/time.cc',
        'src/base/time/time.h',
        'src/base/time/time_posix.cc',
        'src/base/timer/timer.cc',
        'src/base/timer/timer.h',
        'src/base/tracked_objects.cc',
        'src/base/tracked_objects.h',
        'src/base/tracking_info.cc',
        'src/base/tracking_info.h',
        'src/base/tuple.h',
        'src/base/vlog.cc',
        'src/base/vlog.h',
        'src/build/build_config.h',
      ],
    },
    {
      'target_name': 'test_base',
      'type': 'executable',
      'sources': [
        'main.cc',
      ],
      'dependencies': [
        'base',
      ],
    }
  ],
}

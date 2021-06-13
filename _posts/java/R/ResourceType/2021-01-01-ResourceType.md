---
title: ResourceType
permalink: Java/ResourceType
date: 2021-01-11
key: Java.R.ResourceType
category: java
tags: ['java se', 'jdk.management.resource', 'jdk.management.resource', 'clase java', '8u40']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.R.ResourceType.description }}

## Sintaxis
~~~java
@Deprecated(since="10", forRemoval=true) public class ResourceType extends Object
~~~

## Campos
* [DATAGRAM_OPEN](/Java/ResourceType/DATAGRAM_OPEN)
* [DATAGRAM_READ](/Java/ResourceType/DATAGRAM_READ)
* [DATAGRAM_RECEIVED](/Java/ResourceType/DATAGRAM_RECEIVED)
* [DATAGRAM_SENT](/Java/ResourceType/DATAGRAM_SENT)
* [DATAGRAM_WRITE](/Java/ResourceType/DATAGRAM_WRITE)
* [FILE_OPEN](/Java/ResourceType/FILE_OPEN)
* [FILE_READ](/Java/ResourceType/FILE_READ)
* [FILE_WRITE](/Java/ResourceType/FILE_WRITE)
* [FILEDESCRIPTOR_OPEN](/Java/ResourceType/FILEDESCRIPTOR_OPEN)
* [HEAP_ALLOCATED](/Java/ResourceType/HEAP_ALLOCATED)
* [HEAP_RETAINED](/Java/ResourceType/HEAP_RETAINED)
* [SOCKET_OPEN](/Java/ResourceType/SOCKET_OPEN)
* [SOCKET_READ](/Java/ResourceType/SOCKET_READ)
* [SOCKET_WRITE](/Java/ResourceType/SOCKET_WRITE)
* [STDERR_WRITE](/Java/ResourceType/STDERR_WRITE)
* [STDIN_READ](/Java/ResourceType/STDIN_READ)
* [STDOUT_WRITE](/Java/ResourceType/STDOUT_WRITE)
* [THREAD_CPU](/Java/ResourceType/THREAD_CPU)
* [THREAD_CREATED](/Java/ResourceType/THREAD_CREATED)

## Métodos
* [equals()](/Java/ResourceType/equals)
* [getName()](/Java/ResourceType/getName)
* [hashCode()](/Java/ResourceType/hashCode)
* [of()](/Java/ResourceType/of)

## Ejemplo
~~~java
{{ site.data.Java.R.ResourceType.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.ResourceType.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

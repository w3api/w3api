---
title: ThreadMXBean.getThreadInfo()
permalink: /Java/ThreadMXBean-java-lang-management/getThreadInfo/
date: 2021-01-11
key: Java.T.ThreadMXBean-java-lang-management
category: Java
tags: ['java se', 'java.lang.management', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.ThreadMXBean-java-lang-management.metodos valor="getThreadInfo" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
ThreadInfo getThreadInfo(long id)
ThreadInfo[] getThreadInfo(long[] ids)
ThreadInfo[] getThreadInfo(long[] ids, boolean lockedMonitors, boolean lockedSynchronizers)
default ThreadInfo[] getThreadInfo(long[] ids, boolean lockedMonitors, boolean lockedSynchronizers, int maxDepth)
ThreadInfo[] getThreadInfo(long[] ids, int maxDepth)
ThreadInfo getThreadInfo(long id, int maxDepth)
~~~

## Parámetros
* **long id**,  {% include w3api/param_description.html metodo=_dato parametro="long id" %}
* **int maxDepth**,  {% include w3api/param_description.html metodo=_dato parametro="int maxDepth" %}
* **boolean lockedSynchronizers**,  {% include w3api/param_description.html metodo=_dato parametro="boolean lockedSynchronizers" %}
* **boolean lockedMonitors**,  {% include w3api/param_description.html metodo=_dato parametro="boolean lockedMonitors" %}
* **long[] ids**,  {% include w3api/param_description.html metodo=_dato parametro="long[] ids" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

## Clase Padre
[ThreadMXBean](/Java/ThreadMXBean-java-lang-management/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

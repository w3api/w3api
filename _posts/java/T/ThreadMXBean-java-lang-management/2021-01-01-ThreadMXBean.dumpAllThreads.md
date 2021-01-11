---
title: ThreadMXBean.dumpAllThreads()
permalink: Java/ThreadMXBean-java-lang-management/dumpAllThreads
date: 2021-01-11
key: JavaJava.T.ThreadMXBean-java-lang-management
category: java
tags: ['java se', 'java.lang.management', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.ThreadMXBean-java-lang-management.metodos valor="dumpAllThreads" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
ThreadInfo[] dumpAllThreads(boolean lockedMonitors, boolean lockedSynchronizers)
default ThreadInfo[] dumpAllThreads(boolean lockedMonitors, boolean lockedSynchronizers, int maxDepth)
~~~

## Parámetros
* **boolean lockedSynchronizers**,  {% include w3api/param_description.html metodo=_dato parametro="boolean lockedSynchronizers" %}
* **boolean lockedMonitors**,  {% include w3api/param_description.html metodo=_dato parametro="boolean lockedMonitors" %}
* **int maxDepth**,  {% include w3api/param_description.html metodo=_dato parametro="int maxDepth" %}

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

---
title: ThreadMXBean.findDeadlockedThreads()
permalink: /Java/ThreadMXBean-java-lang-management/findDeadlockedThreads/
date: 2021-01-11
key: Java.T.ThreadMXBean-java-lang-management
category: Java
tags: ['java se', 'java.lang.management', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.ThreadMXBean-java-lang-management.metodos valor="findDeadlockedThreads" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
long[] findDeadlockedThreads()
~~~

## Excepciones
[SecurityException](/Java/SecurityException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

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

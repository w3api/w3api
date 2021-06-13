---
title: ThreadMXBean.setThreadAllocatedMemoryEnabled()
permalink: /Java/ThreadMXBean-com-sun-management/setThreadAllocatedMemoryEnabled/
date: 2021-01-11
key: Java.T.ThreadMXBean-com-sun-management
category: Java
tags: ['java se', 'com.sun.management', 'jdk.management', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.ThreadMXBean-com-sun-management.metodos valor="setThreadAllocatedMemoryEnabled" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setThreadAllocatedMemoryEnabled(boolean enable)
~~~

## Parámetros
* **boolean enable**,  {% include w3api/param_description.html metodo=_dato parametro="boolean enable" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

## Clase Padre
[ThreadMXBean](/Java/ThreadMXBean-com-sun-management/)

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

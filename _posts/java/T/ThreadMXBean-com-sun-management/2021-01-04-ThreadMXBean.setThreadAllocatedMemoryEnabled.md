---
title: ThreadMXBean.setThreadAllocatedMemoryEnabled()
permalink: Java/ThreadMXBean-com-sun-management/setThreadAllocatedMemoryEnabled
date: 2021-01-04
key: JavaJava.T.ThreadMXBean-com-sun-management
category: java
tags: ['java se', 'com.sun.management', 'jdk.management', 'metodo java', '6u25']
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
* **boolean enable**,  {% include w3api/param_description.html metodo=_data parametro="boolean enable" %}

## Excepciones
[UnsupportedOperationException](/Java/UnsupportedOperationException/), [SecurityException](/Java/SecurityException/)

## Clase Padre
[ThreadMXBean](/Java/ThreadMXBean-com-sun-management/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.ThreadMXBean-com-sun-management.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

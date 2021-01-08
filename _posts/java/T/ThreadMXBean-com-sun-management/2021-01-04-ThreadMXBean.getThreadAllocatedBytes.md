---
title: ThreadMXBean.getThreadAllocatedBytes()
permalink: Java/ThreadMXBean-com-sun-management/getThreadAllocatedBytes
date: 2021-01-04
key: JavaJava.T.ThreadMXBean-com-sun-management
category: java
tags: ['java se', 'com.sun.management', 'jdk.management', 'metodo java', '6u25']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.ThreadMXBean-com-sun-management.metodos valor="getThreadAllocatedBytes" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
long getThreadAllocatedBytes(long id)
long[] getThreadAllocatedBytes(long[] ids)
~~~

## Parámetros
* **long[] ids**,  {% include w3api/param_description.html metodo=_data parametro="long[] ids" %}
* **long id**,  {% include w3api/param_description.html metodo=_data parametro="long id" %}

## Excepciones
[UnsupportedOperationException](/Java/UnsupportedOperationException/), [NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

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

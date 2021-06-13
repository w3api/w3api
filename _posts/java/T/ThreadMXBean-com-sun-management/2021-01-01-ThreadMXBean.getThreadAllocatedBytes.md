---
title: ThreadMXBean.getThreadAllocatedBytes()
permalink: /Java/ThreadMXBean-com-sun-management/getThreadAllocatedBytes/
date: 2021-01-11
key: Java.T.ThreadMXBean-com-sun-management
category: Java
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
* **long id**,  {% include w3api/param_description.html metodo=_dato parametro="long id" %}
* **long[] ids**,  {% include w3api/param_description.html metodo=_dato parametro="long[] ids" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

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

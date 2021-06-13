---
title: ThreadMXBean.getThreadUserTime()
permalink: Java/ThreadMXBean-com-sun-management/getThreadUserTime
date: 2021-01-11
key: JavaJava.T.ThreadMXBean-com-sun-management
category: java
tags: ['java se', 'com.sun.management', 'jdk.management', 'metodo java', '6u25']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.ThreadMXBean-com-sun-management.metodos valor="getThreadUserTime" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
long[] getThreadUserTime(long[] ids)
~~~

## Parámetros
* **long[] ids**,  {% include w3api/param_description.html metodo=_dato parametro="long[] ids" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/), [NullPointerException](/Java/NullPointerException/)

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
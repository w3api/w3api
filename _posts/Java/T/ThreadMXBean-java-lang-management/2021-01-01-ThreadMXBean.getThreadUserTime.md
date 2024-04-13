---
title: ThreadMXBean.getThreadUserTime()
permalink: /Java/ThreadMXBean-java-lang-management/getThreadUserTime/
date: 2021-01-11
key: Java.T.ThreadMXBean-java-lang-management
category: Java
tags: ['java se', 'java.lang.management', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.ThreadMXBean-java-lang-management.metodos valor="getThreadUserTime" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
long getThreadUserTime(long id)
~~~

## Parámetros
* **long id**,  {% include w3api/param_description.html metodo=_dato parametro="long id" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

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

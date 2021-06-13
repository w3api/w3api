---
title: MethodType.changeParameterType()
permalink: Java/MethodType/changeParameterType
date: 2021-01-11
key: JavaJava.M.MethodType
category: Java
tags: ['java se', 'java.lang.invoke', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MethodType.metodos valor="changeParameterType" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public MethodType changeParameterType(int num, Class<?> nptype)
~~~

## Parámetros
* **int num**,  {% include w3api/param_description.html metodo=_dato parametro="int num" %}
* **Class&lt;?&gt; nptype**,  {% include w3api/param_description.html metodo=_dato parametro="Class<?> nptype" %}

## Excepciones
[IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[MethodType](/Java/MethodType/)

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

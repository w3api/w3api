---
title: MethodType.changeParameterType()
permalink: Java/MethodType/changeParameterType
date: 2021-01-04
key: JavaJava.M.MethodType
category: java
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
* **Class&lt;?&gt; nptype**,  {% include w3api/param_description.html metodo=_data parametro="Class<?> nptype" %}
* **int num**,  {% include w3api/param_description.html metodo=_data parametro="int num" %}

## Excepciones
[IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[MethodType](/Java/MethodType/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MethodType.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

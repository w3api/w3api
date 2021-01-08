---
title: MethodType.insertParameterTypes()
permalink: Java/MethodType/insertParameterTypes
date: 2021-01-04
key: JavaJava.M.MethodType
category: java
tags: ['java se', 'java.lang.invoke', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MethodType.metodos valor="insertParameterTypes" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public MethodType insertParameterTypes(int num, Class<?>... ptypesToInsert)
public MethodType insertParameterTypes(int num, List<Class<?>> ptypesToInsert)
~~~

## Parámetros
* **Class&lt;?&gt;... ptypesToInsert**,  {% include w3api/param_description.html metodo=_data parametro="Class<?>... ptypesToInsert" %}
* **List&lt;Class&lt;?&gt;&gt; ptypesToInsert**,  {% include w3api/param_description.html metodo=_data parametro="List<Class<?>> ptypesToInsert" %}
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

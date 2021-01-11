---
title: Properties.Properties()
permalink: Java/Properties/Properties
date: 2021-01-11
key: JavaJava.P.Properties
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.Properties.constructores valor="Properties" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Properties()
public Properties(int initialCapacity)
public Properties(Properties defaults)
~~~

## Parámetros
* **Properties defaults**,  {% include w3api/param_description.html metodo=_dato parametro="Properties defaults" %}
* **int initialCapacity**,  {% include w3api/param_description.html metodo=_dato parametro="int initialCapacity" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[Properties](/Java/Properties/)

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

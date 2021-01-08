---
title: ResourceBundle.getString()
permalink: Java/ResourceBundle/getString
date: 2021-01-04
key: JavaJava.R.ResourceBundle
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.ResourceBundle.metodos valor="getString" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final String getString(String key)
~~~

## Parámetros
* **String key**,  {% include w3api/param_description.html metodo=_data parametro="String key" %}

## Excepciones
[MissingResourceException](/Java/MissingResourceException/), [ClassCastException](/Java/ClassCastException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[ResourceBundle](/Java/ResourceBundle/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.ResourceBundle.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

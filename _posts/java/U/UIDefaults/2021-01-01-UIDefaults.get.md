---
title: UIDefaults.get()
permalink: Java/UIDefaults/get
date: 2021-01-11
key: JavaJava.U.UIDefaults
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.U.UIDefaults.metodos valor="get" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Object get(Object key)
public Object get(Object key, Locale l)
~~~

## Parámetros
* **Locale l**,  {% include w3api/param_description.html metodo=_dato parametro="Locale l" %}
* **Object key**,  {% include w3api/param_description.html metodo=_dato parametro="Object key" %}

## Clase Padre
[UIDefaults](/Java/UIDefaults/)

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

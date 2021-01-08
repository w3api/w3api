---
title: UIManager.get()
permalink: Java/UIManager/get
date: 2021-01-04
key: JavaJava.U.UIManager
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.U.UIManager.metodos valor="get" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static Object get(Object key)
public static Object get(Object key, Locale l)
~~~

## Parámetros
* **Object key**,  {% include w3api/param_description.html metodo=_data parametro="Object key" %}
* **Locale l**,  {% include w3api/param_description.html metodo=_data parametro="Locale l" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[UIManager](/Java/UIManager/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.U.UIManager.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

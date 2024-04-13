---
title: UIManager.getBoolean()
permalink: /Java/UIManager/getBoolean/
date: 2021-01-11
key: Java.U.UIManager
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.U.UIManager.metodos valor="getBoolean" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static boolean getBoolean(Object key)
public static boolean getBoolean(Object key, Locale l)
~~~

## Parámetros
* **Locale l**,  {% include w3api/param_description.html metodo=_dato parametro="Locale l" %}
* **Object key**,  {% include w3api/param_description.html metodo=_dato parametro="Object key" %}

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
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

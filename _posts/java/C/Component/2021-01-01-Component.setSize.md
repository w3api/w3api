---
title: Component.setSize()
permalink: /Java/Component/setSize/
date: 2021-01-11
key: Java.C.Component
category: Java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Component.metodos valor="setSize" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setSize(int width, int height)
public void setSize(Dimension d)
~~~

## Parámetros
* **int height**,  {% include w3api/param_description.html metodo=_dato parametro="int height" %}
* **Dimension d**,  {% include w3api/param_description.html metodo=_dato parametro="Dimension d" %}
* **int width**,  {% include w3api/param_description.html metodo=_dato parametro="int width" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[Component](/Java/Component/)

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

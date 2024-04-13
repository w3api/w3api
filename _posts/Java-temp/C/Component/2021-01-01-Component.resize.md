---
title: Component.resize()
permalink: /Java/Component/resize/
date: 2021-01-11
key: Java.C.Component
category: Java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Component.metodos valor="resize" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@Deprecated public void resize(int width, int height)
@Deprecated public void resize(Dimension d)
~~~

## Parámetros
* **int height**,  {% include w3api/param_description.html metodo=_dato parametro="int height" %}
* **Dimension d**,  {% include w3api/param_description.html metodo=_dato parametro="Dimension d" %}
* **int width**,  {% include w3api/param_description.html metodo=_dato parametro="int width" %}

## Clase Padre
[Component](/Java/Component/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

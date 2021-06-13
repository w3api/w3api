---
title: PopupMenu.show()
permalink: /Java/PopupMenu/show/
date: 2021-01-11
key: Java.P.PopupMenu
category: java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PopupMenu.metodos valor="show" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void show(Component origin, int x, int y)
~~~

## Parámetros
* **int x**,  {% include w3api/param_description.html metodo=_dato parametro="int x" %}
* **Component origin**,  {% include w3api/param_description.html metodo=_dato parametro="Component origin" %}
* **int y**,  {% include w3api/param_description.html metodo=_dato parametro="int y" %}

## Excepciones
[RuntimeException](/Java/RuntimeException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[PopupMenu](/Java/PopupMenu/)

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

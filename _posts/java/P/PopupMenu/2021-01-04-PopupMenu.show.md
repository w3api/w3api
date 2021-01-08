---
title: PopupMenu.show()
permalink: Java/PopupMenu/show
date: 2021-01-04
key: JavaJava.P.PopupMenu
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
* **int y**,  {% include w3api/param_description.html metodo=_data parametro="int y" %}
* **Component origin**,  {% include w3api/param_description.html metodo=_data parametro="Component origin" %}
* **int x**,  {% include w3api/param_description.html metodo=_data parametro="int x" %}

## Excepciones
[RuntimeException](/Java/RuntimeException/), [NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[PopupMenu](/Java/PopupMenu/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.PopupMenu.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

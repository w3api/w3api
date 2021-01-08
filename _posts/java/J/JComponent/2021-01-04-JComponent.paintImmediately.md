---
title: JComponent.paintImmediately()
permalink: Java/JComponent/paintImmediately
date: 2021-01-04
key: JavaJava.J.JComponent
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JComponent.metodos valor="paintImmediately" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void paintImmediately(int x, int y, int w, int h)
public void paintImmediately(Rectangle r)
~~~

## Parámetros
* **Rectangle r**,  {% include w3api/param_description.html metodo=_data parametro="Rectangle r" %}
* **int y**,  {% include w3api/param_description.html metodo=_data parametro="int y" %}
* **int w**,  {% include w3api/param_description.html metodo=_data parametro="int w" %}
* **int h**,  {% include w3api/param_description.html metodo=_data parametro="int h" %}
* **int x**,  {% include w3api/param_description.html metodo=_data parametro="int x" %}

## Clase Padre
[JComponent](/Java/JComponent/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.J.JComponent.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

---
title: PopupFactory.getPopup()
permalink: Java/PopupFactory/getPopup
date: 2021-01-11
key: JavaJava.P.PopupFactory
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PopupFactory.metodos valor="getPopup" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Popup getPopup(Component owner, Component contents, int x, int y) throws IllegalArgumentException
protected Popup getPopup(Component owner, Component contents, int x, int y, boolean isHeavyWeightPopup) throws IllegalArgumentException
~~~

## Parámetros
* **boolean isHeavyWeightPopup**,  {% include w3api/param_description.html metodo=_dato parametro="boolean isHeavyWeightPopup" %}
* **int y**,  {% include w3api/param_description.html metodo=_dato parametro="int y" %}
* **Component contents**,  {% include w3api/param_description.html metodo=_dato parametro="Component contents" %}
* **Component owner**,  {% include w3api/param_description.html metodo=_dato parametro="Component owner" %}
* **int x**,  {% include w3api/param_description.html metodo=_dato parametro="int x" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[PopupFactory](/Java/PopupFactory/)

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

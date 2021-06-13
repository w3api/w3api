---
title: PlainView.removeUpdate()
permalink: /Java/PlainView/removeUpdate/
date: 2021-01-11
key: Java.P.PlainView
category: Java
tags: ['java se', 'javax.swing.text', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PlainView.metodos valor="removeUpdate" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void removeUpdate(DocumentEvent changes, Shape a, ViewFactory f)
~~~

## Parámetros
* **ViewFactory f**,  {% include w3api/param_description.html metodo=_dato parametro="ViewFactory f" %}
* **Shape a**,  {% include w3api/param_description.html metodo=_dato parametro="Shape a" %}
* **DocumentEvent changes**,  {% include w3api/param_description.html metodo=_dato parametro="DocumentEvent changes" %}

## Clase Padre
[PlainView](/Java/PlainView/)

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

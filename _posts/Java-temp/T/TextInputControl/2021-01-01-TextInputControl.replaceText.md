---
title: TextInputControl.replaceText()
permalink: /Java/TextInputControl/replaceText/
date: 2021-01-11
key: Java.T.TextInputControl
category: Java
tags: ['java se', 'javafx.scene.control', 'javafx.controls', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TextInputControl.metodos valor="replaceText" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void replaceText(int start, int end, String text)
public void replaceText(IndexRange range, String text)
~~~

## Parámetros
* **String text**,  {% include w3api/param_description.html metodo=_dato parametro="String text" %}
* **int end**,  {% include w3api/param_description.html metodo=_dato parametro="int end" %}
* **IndexRange range**,  {% include w3api/param_description.html metodo=_dato parametro="IndexRange range" %}
* **int start**,  {% include w3api/param_description.html metodo=_dato parametro="int start" %}

## Clase Padre
[TextInputControl](/Java/TextInputControl/)

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

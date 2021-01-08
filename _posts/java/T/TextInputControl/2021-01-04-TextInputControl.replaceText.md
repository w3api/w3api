---
title: TextInputControl.replaceText()
permalink: Java/TextInputControl/replaceText
date: 2021-01-04
key: JavaJava.T.TextInputControl
category: java
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
* **int start**,  {% include w3api/param_description.html metodo=_data parametro="int start" %}
* **String text**,  {% include w3api/param_description.html metodo=_data parametro="String text" %}
* **IndexRange range**,  {% include w3api/param_description.html metodo=_data parametro="IndexRange range" %}
* **int end**,  {% include w3api/param_description.html metodo=_data parametro="int end" %}

## Clase Padre
[TextInputControl](/Java/TextInputControl/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.TextInputControl.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

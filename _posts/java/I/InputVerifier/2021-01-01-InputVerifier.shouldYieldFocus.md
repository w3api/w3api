---
title: InputVerifier.shouldYieldFocus()
permalink: Java/InputVerifier/shouldYieldFocus
date: 2021-01-11
key: JavaJava.I.InputVerifier
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.InputVerifier.metodos valor="shouldYieldFocus" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@Deprecated(since="9") public boolean shouldYieldFocus(JComponent input)
public boolean shouldYieldFocus(JComponent source, JComponent target)
~~~

## Parámetros
* **JComponent target**,  {% include w3api/param_description.html metodo=_dato parametro="JComponent target" %}
* **JComponent input**,  {% include w3api/param_description.html metodo=_dato parametro="JComponent input" %}
* **JComponent source**,  {% include w3api/param_description.html metodo=_dato parametro="JComponent source" %}

## Clase Padre
[InputVerifier](/Java/InputVerifier/)

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

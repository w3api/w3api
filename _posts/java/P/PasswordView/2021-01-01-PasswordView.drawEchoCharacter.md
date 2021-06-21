---
title: PasswordView.drawEchoCharacter()
permalink: /Java/PasswordView/drawEchoCharacter/
date: 2021-01-11
key: Java.P.PasswordView
category: Java
tags: ['java se', 'javax.swing.text', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PasswordView.metodos valor="drawEchoCharacter" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected float drawEchoCharacter(Graphics2D g, float x, float y, char c)
@Deprecated(since="9") protected int drawEchoCharacter(Graphics g, int x, int y, char c)
~~~

## Parámetros
* **Graphics g**,  {% include w3api/param_description.html metodo=_dato parametro="Graphics g" %}
* **Graphics2D g**,  {% include w3api/param_description.html metodo=_dato parametro="Graphics2D g" %}
* **float y**,  {% include w3api/param_description.html metodo=_dato parametro="float y" %}
* **int y**,  {% include w3api/param_description.html metodo=_dato parametro="int y" %}
* **float x**,  {% include w3api/param_description.html metodo=_dato parametro="float x" %}
* **char c**,  {% include w3api/param_description.html metodo=_dato parametro="char c" %}
* **int x**,  {% include w3api/param_description.html metodo=_dato parametro="int x" %}

## Clase Padre
[PasswordView](/Java/PasswordView/)

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

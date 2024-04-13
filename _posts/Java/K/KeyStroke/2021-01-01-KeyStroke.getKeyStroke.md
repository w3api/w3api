---
title: KeyStroke.getKeyStroke()
permalink: /Java/KeyStroke/getKeyStroke/
date: 2021-01-11
key: Java.K.KeyStroke
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.K.KeyStroke.metodos valor="getKeyStroke" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static KeyStroke getKeyStroke(char keyChar)
@Deprecated public static KeyStroke getKeyStroke(char keyChar, boolean onKeyRelease)
public static KeyStroke getKeyStroke(int keyCode, int modifiers)
public static KeyStroke getKeyStroke(int keyCode, int modifiers, boolean onKeyRelease)
public static KeyStroke getKeyStroke(Character keyChar, int modifiers)
public static KeyStroke getKeyStroke(String s)
~~~

## Parámetros
* **int modifiers**,  {% include w3api/param_description.html metodo=_dato parametro="int modifiers" %}
* **Character keyChar**,  {% include w3api/param_description.html metodo=_dato parametro="Character keyChar" %}
* **String s**,  {% include w3api/param_description.html metodo=_dato parametro="String s" %}
* **boolean onKeyRelease**,  {% include w3api/param_description.html metodo=_dato parametro="boolean onKeyRelease" %}
* **int keyCode**,  {% include w3api/param_description.html metodo=_dato parametro="int keyCode" %}
* **char keyChar**,  {% include w3api/param_description.html metodo=_dato parametro="char keyChar" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[KeyStroke](/Java/KeyStroke/)

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

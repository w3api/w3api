---
title: KeyStroke.getKeyStroke()
permalink: Java/KeyStroke/getKeyStroke
date: 2021-01-04
key: JavaJava.K.KeyStroke
category: java
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
* **char keyChar**,  {% include w3api/param_description.html metodo=_data parametro="char keyChar" %}
* **Character keyChar**,  {% include w3api/param_description.html metodo=_data parametro="Character keyChar" %}
* **int modifiers**,  {% include w3api/param_description.html metodo=_data parametro="int modifiers" %}
* **int keyCode**,  {% include w3api/param_description.html metodo=_data parametro="int keyCode" %}
* **String s**,  {% include w3api/param_description.html metodo=_data parametro="String s" %}
* **boolean onKeyRelease**,  {% include w3api/param_description.html metodo=_data parametro="boolean onKeyRelease" %}

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
{%- for _ldc in site.data.Java.K.KeyStroke.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

---
title: JTextComponent.loadKeymap()
permalink: Java/JTextComponent/loadKeymap
date: 2021-01-11
key: JavaJava.J.JTextComponent
category: java
tags: ['java se', 'javax.swing.text', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JTextComponent.metodos valor="loadKeymap" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static void loadKeymap(Keymap map, JTextComponent.KeyBinding[] bindings, Action[] actions)
~~~

## Parámetros
* **Keymap map**,  {% include w3api/param_description.html metodo=_dato parametro="Keymap map" %}
* **Action[] actions**,  {% include w3api/param_description.html metodo=_dato parametro="Action[] actions" %}
* **JTextComponent.KeyBinding[] bindings**,  {% include w3api/param_description.html metodo=_dato parametro="JTextComponent.KeyBinding[] bindings" %}

## Clase Padre
[JTextComponent](/Java/JTextComponent/)

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

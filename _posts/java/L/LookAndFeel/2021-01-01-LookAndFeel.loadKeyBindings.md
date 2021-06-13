---
title: LookAndFeel.loadKeyBindings()
permalink: /Java/LookAndFeel/loadKeyBindings/
date: 2021-01-11
key: Java.L.LookAndFeel
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LookAndFeel.metodos valor="loadKeyBindings" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static void loadKeyBindings(InputMap retMap, Object[] keys)
~~~

## Parámetros
* **InputMap retMap**,  {% include w3api/param_description.html metodo=_dato parametro="InputMap retMap" %}
* **Object[] keys**,  {% include w3api/param_description.html metodo=_dato parametro="Object[] keys" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[LookAndFeel](/Java/LookAndFeel/)

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

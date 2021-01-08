---
title: KeyStroke.getKeyStrokeForEvent()
permalink: Java/KeyStroke/getKeyStrokeForEvent
date: 2021-01-04
key: JavaJava.K.KeyStroke
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.K.KeyStroke.metodos valor="getKeyStrokeForEvent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static KeyStroke getKeyStrokeForEvent(KeyEvent anEvent)
~~~

## Parámetros
* **KeyEvent anEvent**,  {% include w3api/param_description.html metodo=_data parametro="KeyEvent anEvent" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

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

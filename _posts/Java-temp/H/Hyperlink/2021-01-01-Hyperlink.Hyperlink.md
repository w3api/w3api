---
title: Hyperlink.Hyperlink()
permalink: /Java/Hyperlink/Hyperlink/
date: 2021-01-11
key: Java.H.Hyperlink
category: Java
tags: ['java se', 'javafx.scene.control', 'javafx.controls', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.Hyperlink.constructores valor="Hyperlink" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Hyperlink()
public Hyperlink(String text)
public Hyperlink(String text, Node graphic)
~~~

## Parámetros
* **String text**,  {% include w3api/param_description.html metodo=_dato parametro="String text" %}
* **Node graphic**,  {% include w3api/param_description.html metodo=_dato parametro="Node graphic" %}

## Clase Padre
[Hyperlink](/Java/Hyperlink/)

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

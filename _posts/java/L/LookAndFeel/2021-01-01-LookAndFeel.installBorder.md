---
title: LookAndFeel.installBorder()
permalink: /Java/LookAndFeel/installBorder/
date: 2021-01-11
key: Java.L.LookAndFeel
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LookAndFeel.metodos valor="installBorder" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static void installBorder(JComponent c, String defaultBorderName)
~~~

## Parámetros
* **String defaultBorderName**,  {% include w3api/param_description.html metodo=_dato parametro="String defaultBorderName" %}
* **JComponent c**,  {% include w3api/param_description.html metodo=_dato parametro="JComponent c" %}

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

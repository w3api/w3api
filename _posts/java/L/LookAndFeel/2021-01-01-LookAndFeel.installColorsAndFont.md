---
title: LookAndFeel.installColorsAndFont()
permalink: /Java/LookAndFeel/installColorsAndFont/
date: 2021-01-11
key: Java.L.LookAndFeel
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LookAndFeel.metodos valor="installColorsAndFont" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static void installColorsAndFont(JComponent c, String defaultBgName, String defaultFgName, String defaultFontName)
~~~

## Parámetros
* **String defaultBgName**,  {% include w3api/param_description.html metodo=_dato parametro="String defaultBgName" %}
* **JComponent c**,  {% include w3api/param_description.html metodo=_dato parametro="JComponent c" %}
* **String defaultFontName**,  {% include w3api/param_description.html metodo=_dato parametro="String defaultFontName" %}
* **String defaultFgName**,  {% include w3api/param_description.html metodo=_dato parametro="String defaultFgName" %}

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

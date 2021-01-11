---
title: LookAndFeel.installColors()
permalink: Java/LookAndFeel/installColors
date: 2021-01-11
key: JavaJava.L.LookAndFeel
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LookAndFeel.metodos valor="installColors" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static void installColors(JComponent c, String defaultBgName, String defaultFgName)
~~~

## Parámetros
* **String defaultBgName**,  {% include w3api/param_description.html metodo=_dato parametro="String defaultBgName" %}
* **JComponent c**,  {% include w3api/param_description.html metodo=_dato parametro="JComponent c" %}
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
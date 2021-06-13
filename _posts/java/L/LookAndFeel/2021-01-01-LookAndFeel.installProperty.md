---
title: LookAndFeel.installProperty()
permalink: /Java/LookAndFeel/installProperty/
date: 2021-01-11
key: Java.L.LookAndFeel
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LookAndFeel.metodos valor="installProperty" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static void installProperty(JComponent c, String propertyName, Object propertyValue)
~~~

## Parámetros
* **String propertyName**,  {% include w3api/param_description.html metodo=_dato parametro="String propertyName" %}
* **JComponent c**,  {% include w3api/param_description.html metodo=_dato parametro="JComponent c" %}
* **Object propertyValue**,  {% include w3api/param_description.html metodo=_dato parametro="Object propertyValue" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [ClassCastException](/Java/ClassCastException/), [NullPointerException](/Java/NullPointerException/)

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

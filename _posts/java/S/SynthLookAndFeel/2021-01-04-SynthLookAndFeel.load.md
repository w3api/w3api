---
title: SynthLookAndFeel.load()
permalink: Java/SynthLookAndFeel/load
date: 2021-01-04
key: JavaJava.S.SynthLookAndFeel
category: java
tags: ['java se', 'javax.swing.plaf.synth', 'java.desktop', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SynthLookAndFeel.metodos valor="load" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void load(InputStream input, Class<?> resourceBase) throws ParseException
public void load(URL url) throws ParseException, IOException
~~~

## Parámetros
* **InputStream input**,  {% include w3api/param_description.html metodo=_data parametro="InputStream input" %}
* **URL url**,  {% include w3api/param_description.html metodo=_data parametro="URL url" %}
* **Class&lt;?&gt; resourceBase**,  {% include w3api/param_description.html metodo=_data parametro="Class<?> resourceBase" %}

## Excepciones
[IOException](/Java/IOException/), [ParseException](/Java/ParseException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[SynthLookAndFeel](/Java/SynthLookAndFeel/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SynthLookAndFeel.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

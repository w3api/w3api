---
title: FormatConversionProvider.getTargetFormats()
permalink: Java/FormatConversionProvider/getTargetFormats
date: 2021-01-04
key: JavaJava.F.FormatConversionProvider
category: java
tags: ['java se', 'javax.sound.sampled.spi', 'java.desktop', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FormatConversionProvider.metodos valor="getTargetFormats" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract AudioFormat[] getTargetFormats(AudioFormat.Encoding targetEncoding, AudioFormat sourceFormat)
~~~

## Parámetros
* **AudioFormat.Encoding targetEncoding**,  {% include w3api/param_description.html metodo=_data parametro="AudioFormat.Encoding targetEncoding" %}
* **AudioFormat sourceFormat**,  {% include w3api/param_description.html metodo=_data parametro="AudioFormat sourceFormat" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[FormatConversionProvider](/Java/FormatConversionProvider/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.F.FormatConversionProvider.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

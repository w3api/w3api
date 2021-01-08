---
title: FormatConversionProvider.getAudioInputStream()
permalink: Java/FormatConversionProvider/getAudioInputStream
date: 2021-01-04
key: JavaJava.F.FormatConversionProvider
category: java
tags: ['java se', 'javax.sound.sampled.spi', 'java.desktop', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FormatConversionProvider.metodos valor="getAudioInputStream" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract AudioInputStream getAudioInputStream(AudioFormat.Encoding targetEncoding, AudioInputStream sourceStream)
public abstract AudioInputStream getAudioInputStream(AudioFormat targetFormat, AudioInputStream sourceStream)
~~~

## Parámetros
* **AudioFormat targetFormat**,  {% include w3api/param_description.html metodo=_data parametro="AudioFormat targetFormat" %}
* **AudioFormat.Encoding targetEncoding**,  {% include w3api/param_description.html metodo=_data parametro="AudioFormat.Encoding targetEncoding" %}
* **AudioInputStream sourceStream**,  {% include w3api/param_description.html metodo=_data parametro="AudioInputStream sourceStream" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

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

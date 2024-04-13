---
title: FormatConversionProvider.getAudioInputStream()
permalink: /Java/FormatConversionProvider/getAudioInputStream/
date: 2021-01-11
key: Java.F.FormatConversionProvider
category: Java
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
* **AudioFormat.Encoding targetEncoding**,  {% include w3api/param_description.html metodo=_dato parametro="AudioFormat.Encoding targetEncoding" %}
* **AudioFormat targetFormat**,  {% include w3api/param_description.html metodo=_dato parametro="AudioFormat targetFormat" %}
* **AudioInputStream sourceStream**,  {% include w3api/param_description.html metodo=_dato parametro="AudioInputStream sourceStream" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[FormatConversionProvider](/Java/FormatConversionProvider/)

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

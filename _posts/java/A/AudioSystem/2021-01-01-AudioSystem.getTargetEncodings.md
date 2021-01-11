---
title: AudioSystem.getTargetEncodings()
permalink: Java/AudioSystem/getTargetEncodings
date: 2021-01-11
key: JavaJava.A.AudioSystem
category: java
tags: ['java se', 'javax.sound.sampled', 'java.desktop', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AudioSystem.metodos valor="getTargetEncodings" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static AudioFormat.Encoding[] getTargetEncodings(AudioFormat sourceFormat)
public static AudioFormat.Encoding[] getTargetEncodings(AudioFormat.Encoding sourceEncoding)
~~~

## Parámetros
* **AudioFormat sourceFormat**,  {% include w3api/param_description.html metodo=_dato parametro="AudioFormat sourceFormat" %}
* **AudioFormat.Encoding sourceEncoding**,  {% include w3api/param_description.html metodo=_dato parametro="AudioFormat.Encoding sourceEncoding" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[AudioSystem](/Java/AudioSystem/)

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

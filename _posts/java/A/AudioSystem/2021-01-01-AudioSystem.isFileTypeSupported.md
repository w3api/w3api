---
title: AudioSystem.isFileTypeSupported()
permalink: Java/AudioSystem/isFileTypeSupported
date: 2021-01-11
key: JavaJava.A.AudioSystem
category: java
tags: ['java se', 'javax.sound.sampled', 'java.desktop', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AudioSystem.metodos valor="isFileTypeSupported" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static boolean isFileTypeSupported(AudioFileFormat.Type fileType)
public static boolean isFileTypeSupported(AudioFileFormat.Type fileType, AudioInputStream stream)
~~~

## Parámetros
* **AudioFileFormat.Type fileType**,  {% include w3api/param_description.html metodo=_dato parametro="AudioFileFormat.Type fileType" %}
* **AudioInputStream stream**,  {% include w3api/param_description.html metodo=_dato parametro="AudioInputStream stream" %}

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

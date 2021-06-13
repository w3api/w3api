---
title: AudioSystem.getTargetFormats()
permalink: /Java/AudioSystem/getTargetFormats/
date: 2021-01-11
key: Java.A.AudioSystem
category: Java
tags: ['java se', 'javax.sound.sampled', 'java.desktop', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AudioSystem.metodos valor="getTargetFormats" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static AudioFormat[] getTargetFormats(AudioFormat.Encoding targetEncoding, AudioFormat sourceFormat)
~~~

## Parámetros
* **AudioFormat.Encoding targetEncoding**,  {% include w3api/param_description.html metodo=_dato parametro="AudioFormat.Encoding targetEncoding" %}
* **AudioFormat sourceFormat**,  {% include w3api/param_description.html metodo=_dato parametro="AudioFormat sourceFormat" %}

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

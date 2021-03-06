---
title: AudioSystem.getTargetDataLine()
permalink: /Java/AudioSystem/getTargetDataLine/
date: 2021-01-11
key: Java.A.AudioSystem
category: Java
tags: ['java se', 'javax.sound.sampled', 'java.desktop', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AudioSystem.metodos valor="getTargetDataLine" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static TargetDataLine getTargetDataLine(AudioFormat format) throws LineUnavailableException
public static TargetDataLine getTargetDataLine(AudioFormat format, Mixer.Info mixerinfo) throws LineUnavailableException
~~~

## Parámetros
* **AudioFormat format**,  {% include w3api/param_description.html metodo=_dato parametro="AudioFormat format" %}
* **Mixer.Info mixerinfo**,  {% include w3api/param_description.html metodo=_dato parametro="Mixer.Info mixerinfo" %}

## Excepciones
[LineUnavailableException](/Java/LineUnavailableException/), [SecurityException](/Java/SecurityException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

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

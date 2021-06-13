---
title: AudioSystem.getMixer()
permalink: /Java/AudioSystem/getMixer/
date: 2021-01-11
key: Java.A.AudioSystem
category: Java
tags: ['java se', 'javax.sound.sampled', 'java.desktop', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AudioSystem.metodos valor="getMixer" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static Mixer getMixer(Mixer.Info info)
~~~

## Parámetros
* **Mixer.Info info**,  {% include w3api/param_description.html metodo=_dato parametro="Mixer.Info info" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

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

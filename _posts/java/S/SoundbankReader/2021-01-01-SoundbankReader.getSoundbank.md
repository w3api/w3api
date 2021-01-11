---
title: SoundbankReader.getSoundbank()
permalink: Java/SoundbankReader/getSoundbank
date: 2021-01-11
key: JavaJava.S.SoundbankReader
category: java
tags: ['java se', 'javax.sound.midi.spi', 'java.desktop', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SoundbankReader.metodos valor="getSoundbank" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract Soundbank getSoundbank(File file) throws InvalidMidiDataException, IOException
public abstract Soundbank getSoundbank(InputStream stream) throws InvalidMidiDataException, IOException
public abstract Soundbank getSoundbank(URL url) throws InvalidMidiDataException, IOException
~~~

## Parámetros
* **URL url**,  {% include w3api/param_description.html metodo=_dato parametro="URL url" %}
* **File file**,  {% include w3api/param_description.html metodo=_dato parametro="File file" %}
* **InputStream stream**,  {% include w3api/param_description.html metodo=_dato parametro="InputStream stream" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [InvalidMidiDataException](/Java/InvalidMidiDataException/), [IOException](/Java/IOException/)

## Clase Padre
[SoundbankReader](/Java/SoundbankReader/)

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

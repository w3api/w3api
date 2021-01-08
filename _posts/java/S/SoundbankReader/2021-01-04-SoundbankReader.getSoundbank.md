---
title: SoundbankReader.getSoundbank()
permalink: Java/SoundbankReader/getSoundbank
date: 2021-01-04
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
* **URL url**,  {% include w3api/param_description.html metodo=_data parametro="URL url" %}
* **InputStream stream**,  {% include w3api/param_description.html metodo=_data parametro="InputStream stream" %}
* **File file**,  {% include w3api/param_description.html metodo=_data parametro="File file" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IOException](/Java/IOException/), [InvalidMidiDataException](/Java/InvalidMidiDataException/)

## Clase Padre
[SoundbankReader](/Java/SoundbankReader/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SoundbankReader.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>

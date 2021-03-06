---
title: Sequencer.setSequence()
permalink: /Java/Sequencer/setSequence/
date: 2021-01-11
key: Java.S.Sequencer
category: Java
tags: ['java se', 'javax.sound.midi', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.Sequencer.metodos valor="setSequence" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setSequence(InputStream stream) throws IOException, InvalidMidiDataException
void setSequence(Sequence sequence) throws InvalidMidiDataException
~~~

## Parámetros
* **Sequence sequence**,  {% include w3api/param_description.html metodo=_dato parametro="Sequence sequence" %}
* **InputStream stream**,  {% include w3api/param_description.html metodo=_dato parametro="InputStream stream" %}

## Excepciones
[InvalidMidiDataException](/Java/InvalidMidiDataException/), [IOException](/Java/IOException/)

## Clase Padre
[Sequencer](/Java/Sequencer/)

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
